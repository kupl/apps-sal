N, K = map(int, input().split())
D = set(input().split())
E = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"} - D
result = False
while result == False:
    for i in str(N):
        if not i in E:
            N = N + 1
            result = False
            break
        else:
            result = True
print(N)
