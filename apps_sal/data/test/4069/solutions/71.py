X, K, D = map(int, input().split())


cnt = min(abs(X) // D, K)
c_K = K

c_K -= cnt
rem = abs(X) - D * cnt

if c_K % 2 == 0:
    print(rem)
else:
    print(abs(rem - D))
