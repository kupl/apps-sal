a,b,c,d=  list(map(int, input().split()))

Max_ac = a*c
Max_ad = a*d
Max_bc = b*c
Max_bd = b*d

Max_list = [Max_ac,Max_ad,Max_bc,Max_bd] 
 
print((max(Max_list)))

