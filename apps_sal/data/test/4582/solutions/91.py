# 056a

# a=H, b=H TCD君は正直者
# a=H, b=D TCD君は嘘つき
# a=D, b=H TCD君は嘘つき
# a=D, b=D TCD君は正直者

a, b = list(map(str, input().split()))

if a == 'H' and b == 'H':
    print('H')
elif a == 'H' and b == 'D':
    print('D')
elif a == 'D' and b == 'H':
    print('D')
else:
    print('H')

