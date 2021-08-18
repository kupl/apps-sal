memo = [[0] * 10 for i in range(10)]


def kazu(start_num, end_num):
    nonlocal memo
    if memo[start_num][end_num] > 0:
        # print('memo',start_num,end_num)
        return memo[start_num][end_num]
    else:
        ans = 0
        # 1桁
        if start_num == end_num:
            if start_num <= n:
                # print(start_num)
                ans += 1
        # 2桁
        if start_num * 10 + end_num <= n:
            #print(start_num * 10 + end_num)
            ans += 1
        # 3桁
        for i in range(10):
            if start_num * 100 + i * 10 + end_num <= n:
                #print(start_num * 100 + end_num)
                ans += 1
            else:
                break
        # 4桁
        for i in range(100):
            if start_num * 1000 + i * 10 + end_num <= n:
                #print(start_num * 1000 + end_num)
                ans += 1
            else:
                break
        # 5桁
        for i in range(1000):
            if start_num * 10000 + i * 10 + end_num <= n:
                #print(start_num * 10000 + end_num)
                ans += 1
            else:
                break
        # 6桁
        for i in range(10000):
            if start_num * 100000 + i * 10 + end_num <= n:
                #print(start_num * 10000 + end_num)
                ans += 1
            else:
                break
        memo[start_num][end_num] = ans
        # print(start_num,end_num,'---',ans)
        return ans


n = int(input())
str_n = str(n)
kotae = 0
# print(memo)
for a in range(1, n + 1):
    if a % 10 != 0:
        str_a = str(a)
        # print('-----',a,'-----',int(str_a[-1]),int(str_a[0]))
        kotae += kazu(int(str_a[-1]), int(str_a[0]))
        # print(memo)
print(kotae)
