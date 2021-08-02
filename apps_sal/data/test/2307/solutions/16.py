n = int(input())
arr = list(map(int, input().split()))
odd = even = 0
for each in arr:
    if each % 2:
        odd += 1
    else:
        even += 1

if even > odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
