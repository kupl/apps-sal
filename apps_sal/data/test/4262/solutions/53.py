def cal_A(num):
    ans = 1
    for i in range(num, 0, -1):
        ans *= i
    print(ans)


def cal_B(num):
    ans = 1
    for i in range(num, 0, -1):
        ans *= i
    ans = ans // num
    return ans


def cal_C(list_a):
    ans = 0
    for i in list_a:
        target_list1 = list_a[list_a.index(i):]
        target_list2 = sorted(target_list1)
        a = int(target_list2.index(i))
        ans += a * cal_B(len(target_list1))
    return ans + 1


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

print(abs(cal_C(P) - cal_C(Q)))
