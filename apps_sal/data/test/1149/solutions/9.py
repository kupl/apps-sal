arr = [False] * int(input())
for j in range(2):
    for i in list(map(int, input().split()))[1:]:
        arr[i - 1] = True
if False in arr:
    print('Oh, my keyboard!')
else:
    print('I become the guy.')
