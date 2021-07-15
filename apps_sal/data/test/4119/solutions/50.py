n, m = map(int, input().split())
xl = sorted(list(map(int, input().split())))

delta = []
for i in range(m-1):
    delta.append(abs(xl[i]-xl[i+1]))
delta.sort(reverse=True)
print(sum(delta[n-1:]))
