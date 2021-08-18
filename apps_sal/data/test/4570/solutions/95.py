S_list = list(map(int, input().split()))
N, A, B = S_list
if N * A > B:
    result = B
else:
    result = N * A
print(result)
