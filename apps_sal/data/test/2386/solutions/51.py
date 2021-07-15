#C
import statistics
N = int(input())
A = list(map(int, input().split()))

# abs(A[i]-i+b)より、
# bは(A[i]-i)リストの中央値
As = []
for i in range(N):
    As.append(A[i] - (i + 1))
mid = int(statistics.median(As))

result = 0
for i in range(N):
    result += abs(A[i] - (mid + i + 1))
print(result)

