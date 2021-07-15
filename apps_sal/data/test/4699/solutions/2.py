N, K = map(int, input().split())
unlike_list = set(map(str, input().split()))

def judge(num):
    for i in str(num):
        if i in unlike_list:
            return False
    return True

ans = False
while not ans:
    if judge(N):
        ans = True
    else:
        N += 1

print(N)
