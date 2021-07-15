n = int(input())
mt = dict()

for i in range(n):
    line = input()
    if line in mt:
        mt[line] += 1
    else:
        mt[line] = 1

print(max(mt.values()))
