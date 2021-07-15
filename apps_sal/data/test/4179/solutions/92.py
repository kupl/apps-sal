N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
print((sum(sum(i * j for i, j in zip(list(map(int, input().split())), B)) > -C for k in range(N))))

