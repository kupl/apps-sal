n = int(input())
inp, k = {}, 0


s = input().split()

for i in range(0, len(s)):
    item = int(s[i])
    if item in inp:
        inp[item] += [i]
    else:
        inp[item] = [i]

inp_keys = [int(i) for i in inp.keys()]
inp_keys.sort()
result = []


def check(arr):
    diff = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != diff:
            return False
    return diff


for i in inp_keys:
    j = inp[i]
    if len(j) == 1:
        result.append([i, 0])
        continue
    diff = check(j)
    if diff:
        result.append([i, diff])

out = ""
for i, j in result:
    out += str(i) + " " + str(j) + "\n"

print(len(result))
print(out[:-1])
