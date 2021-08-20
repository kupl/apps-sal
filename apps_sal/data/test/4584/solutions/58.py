N = int(input())
A = list(map(int, input().split()))
answer = [0] * N
for i in A:
    answer[i - 1] += 1
for n in answer:
    print(n)
