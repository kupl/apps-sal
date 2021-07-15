n = int(input())
a = input()
b = input()

i = n//2
if(n%2 == 0):
    i -= 1
cnt = 0
while i > -1:
    set_a = {a[i], a[-i-1]}
    set_b = {b[i], b[-i-1]}
    if len(set_a) == 1:
        if len(set_b) != 1:
            if (a[i] == b[i]) or (a[i] == b[-i-1]):
                cnt += 1
            else:
                cnt += 2
        if (len(set_b) == 1) and (n%2 == 1) and (n//2 == i) and (set_a != set_b):
            cnt += 1
    if len(set_a) == 2:
        if len(set_b) == 1:
            cnt += 1
        if len(set_b) == 2:
            common = set_a.intersection(set_b)
            if len(common) == 0:
                cnt += 2
            if len(common) == 1:
                cnt += 1
                
    i -= 1
print(cnt)    

