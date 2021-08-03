# cook your dish here
jc, sc, m = map(int, input().split())
n = (m - jc) // sc
if n % 2 == 0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")
