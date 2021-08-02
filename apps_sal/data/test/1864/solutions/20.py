count = input()
nominals_str = input().strip().split(" ")
nominals = [int(i) for i in nominals_str]

minimal = min(nominals)
if minimal == 1:
    print(-1)
else:
    print(1)
