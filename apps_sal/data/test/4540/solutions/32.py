n = int(input())
lst = list(map(int, input().split()))
s = 0
diff_lst = []
sign_lst = []
for i in lst + [0]:
    diff = i - s
    diff_lst.append(abs(diff))
    sign_lst.append(1) if diff > 0 else sign_lst.append(-1)
    s = i
su = sum(diff_lst)
for i in range(n):
    if sign_lst[i] * sign_lst[i + 1] > 0:
        print(su)
    else:
        print(su - diff_lst[i] - diff_lst[i + 1] + abs(diff_lst[i] - diff_lst[i + 1]))
