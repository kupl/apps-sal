def is_sorted(li):
    temp = list(li)
    for i in range(0, len(li)):
        if li[i] != temp[i]:
            return False
    return True


def process():
    (n, k) = list(map(int, input().split()))
    li = list(map(int, input().split()))
    if is_sorted(li) == False:
        print('-1')
        return
    elif k == 1 and len(set(li)) == 1:
        print('1')
        return
    elif k > 1:
        ans = 0
        s = len(set(li))
        ans = 1
        s -= k
        while s > 0:
            ans += 1
            s -= k - 1
        print(ans)
    else:
        print('-1')
        return


tests = int(input())
for i in range(tests):
    process()
