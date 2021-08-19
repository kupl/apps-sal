x = [500, 1000, 1500, 2000, 2500]
m = list(map(int, input().split()))
w = list(map(int, input().split()))
(hs, hu) = map(int, input().split())
print(sum((max(3 * x[i] // 10, x[i] - x[i] * m[i] // 250 - 50 * w[i]) for i in range(5))) + hs * 100 - hu * 50)
