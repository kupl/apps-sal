def IsInTime(d, t, s: int) -> bool:
    if s * t >= d:
        return True
    else:
        return False


d, t, s = list(map(int, input().split()))
if IsInTime(d, t, s):
    print("Yes")
else:
    print("No")
