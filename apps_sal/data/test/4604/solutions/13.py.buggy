mod = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))
c_dic = dict()
if n % 2 == 0:
    for num in a:
        if num % 2 == 0 or n < num:
            print(0)
            return
        if num in c_dic:
            c_dic[num] += 1
            if c_dic[num] > 2:
                print(0)
                return
        else:
            c_dic[num] = 1
    print(pow(2, n // 2, mod))
else:
    for num in a:
        if num % 2 == 1 or n < num:
            print(0)
            return
        if num in c_dic:
            c_dic[num] += 1
            if c_dic[num] > 2:
                print(0)
                return
        else:
            c_dic[num] = 1
    if c_dic[0] != 1:
        print(0)
        return
    print(pow(2, n // 2, mod))
