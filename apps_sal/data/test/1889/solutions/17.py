def func(a):
    s=0
    per= 0
    for i in range(len(a)):
        if a[i] == '1':
            
            per+=1
        else:
            s=max(s, per)
            per=0
    s=max(per, s)
    return s
def main(a):
    A= []
    B = [0] * int(a[0])
    for i in range(int(a[0])):
        A.append(input().split())
    for i in range(int(a[0])):
        B[i] = func(A[i])
    for i in range(int(a[2])):
        s = 0
        k = input().split()
        A[int(k[0]) - 1][int(k[1]) - 1] = str((int(A[int(k[0]) - 1][int(k[1]) - 1]) + 1) % 2)
        B[int(k[0]) - 1] = func(A[int(k[0]) - 1])
        for i in B:
            s = max(s, i)
        print(s)
a =input().split()
main(a)
