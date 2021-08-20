N = int(input())
H = list(map(int, input().split()))
print(sum((H[i] >= max(H[:i] + [0]) for i in range(N))))
