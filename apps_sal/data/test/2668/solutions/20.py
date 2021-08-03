# cook your dish here
j, s, m = map(int, input().split())
if ((m - j) // s) % 2 == 0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")
