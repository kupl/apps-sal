N = int(input())
T = input()
V = 10**10
if T == "1":
    print(2 * V); return
elif T == "11" or T == "0":
    print(V); return
else:
    K = T.count("0")
    data = '110' * (K + 1)
    if data.count(T) == 0:
        print(0)
    else:

        if T[-1] == '0':
            print(10**10 - K + 1)
        else:
            print(10**10 - K)
