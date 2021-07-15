a = int(input())
for i in range(a):
    s1 = set()
    ans = 0
    l = input()
    now = input().split()
    for i in now:
        k =int(i) 
        while k%2==0 and k not in s1:
            s1.add(k)
            k=k//2
    print(len(s1))
