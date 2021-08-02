from sys import stdin, stdout
MOD = 10**9 + 7


def find(arr, N):
    R = [0, 0, 0]
    Z = 1
    for i in arr:
        if i == 'a': R[0] += Z
        if i == 'b': R[1] = (R[1] + R[0]) % MOD
        if i == 'c': R[2] = (R[2] + R[1]) % MOD
        if i == '?':
            a, b, c = R[:], R[:], R[:]
            a[0] = (a[0] + Z) % MOD
            b[1] = (b[1] + b[0]) % MOD
            c[2] = (c[2] + c[1]) % MOD
            R = [(a[i] + b[i] + c[i]) % MOD for i in range(3)]
            Z = Z * 3 % MOD
            # print(a)
            # print(b)
            # print(c)
        # print(R)
    return R[2] % MOD


def main():
    # for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    arr = stdin.readline().strip()
    print(find(arr, N))


main()


# H=[]
# def bt(i,s):
#     if i==2:
#         return H.append(s)
#     bt(i+1,s+"a")
#     bt(i+1,s+"b")
#     bt(i+1,s+"c")
# bt(0,"")
# print(H)
# F=0
# X=[0,0,0]
# for j in H:
#     R=[0,0,0]
#     for i in j:
#         if i=='a': R[0]+=1
#         if i=='b': R[1]+=R[0]
#         if i=='c': R[2]+=R[1]
#     F+=R[2]
#     X=[X[i]+R[i] for i in range(3)]
# print(X)
# print(F)
