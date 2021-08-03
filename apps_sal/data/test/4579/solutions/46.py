N = int(input())

dics = {}

for _ in range(N):
    s = input()
    if s in dics:
        dics[s] += 1
    else:
        dics[s] = 1
print(len(dics.keys()))
