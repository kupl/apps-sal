(n, k, x) = map(int, input().split())
Time = list(map(int, input().split()))
rez = sum(Time[0:n - k]) + k * x
print(rez)
