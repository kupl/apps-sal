s = int(input())
for i in range(s):
    hh,mm = list(map(int, input().split()))
    ms = hh*60+mm
    print(24*60-ms)

