n, x = list(map(int, input().split()))

data = list(map(int, input().split()))

s = set(data)

if len(s) < len(data):
    print(0)
    return


answer = -1

ss = set()
prevs = set()

for el in data:
    curr = el & x

    if curr in prevs or el in ss:
        answer = 1

    prevs.add(el)

    if curr in ss and answer != 1:
        answer = 2

    ss.add(curr)

print(answer)
