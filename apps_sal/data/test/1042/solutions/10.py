def bin_pow(num, degree , module):
    if degree == 0:
        return 1
    if degree == 1:
        return num % module

    if degree % 2 == 0:
        val = bin_pow(num, degree // 2, module)
        return (val * val) % module
    
    return (num * bin_pow(num , degree - 1, module)) % module



x, y = list(map(int,input().split()))


if y % x != 0:
    print(0)
    return

y //= x

divs = set()
to_gen = []

num = 2
val = y

while num * num <= val:
    degree = 0
    while y % num == 0:
        degree+=1
        y //= num
    if degree != 0:
        to_gen.append((num, degree))

    if num == 2:
        num += 1
    else:
        num += 2

if y != 1:
    to_gen.append((y, 1))

    
to_gen_len = len(to_gen)

def generate(ind):
    if ind == to_gen_len:
        yield 1
        return 
    gen_val = to_gen[ind][0]
    
    for deg in range(1 + to_gen[ind][1]):
        for each in generate(ind  + 1):
            yield gen_val**deg * each

for each in generate(0):
    divs.add(each)

divs = list(divs)
divs.sort()
divs_answers = {}
mod = 10**9 + 7
ans = bin_pow(2, val - 1, mod)

for el in divs:
    if el == 1:
        divs_answers[el] = 1
        ans -= 1
    else:
        curr_val = bin_pow(2, el - 1 ,mod)
        for other_el in divs:
            if other_el >= el:
                break
            if el % other_el !=0:
                continue
            
            curr_val -= divs_answers[other_el]

        divs_answers[el] = curr_val % mod
        ans -= curr_val

print(divs_answers[val])

