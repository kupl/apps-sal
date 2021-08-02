a, b = input().split()
a_num, b_num = map(int, input().split())
c = input()
if(c == a):
    a_num -= 1
else:
    b_num -= 1
print(a_num, b_num)
