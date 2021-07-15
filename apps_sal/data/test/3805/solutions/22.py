s = input()

if len(s)%2:print('No');return

if s[::2].count('+')-s[1::2].count('+')==0:print('Yes');return

print('No')





# Made By Mostafa_Khaled

