N = int(input())
L = list(map(int, input().split()))
if max(L) < sum(L) - max(L):
    answer = 'Yes'
else:
    answer = 'No'
print(answer)
