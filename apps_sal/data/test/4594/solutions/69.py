N = int(input())
m = []
for i in range(N):
    m.append(int(input()))
m = sorted(set(m))
print(len(m))
