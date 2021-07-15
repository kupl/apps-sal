n = int(input())

arr = list(map(int, input().split()))

odd_num = len([e for e in arr if e % 2 != 0])
four_num = len([e for e in arr if e % 4 == 0])
even_num = n - odd_num - four_num

if even_num:
    print("Yes" if four_num >= odd_num else "No")
else:
    print("Yes" if four_num >= odd_num - 1 else "No")
