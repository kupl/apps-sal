n = int(input())
result_dict = {'AC':0,'WA':0,'TLE':0,'RE':0}
for i in range(n):
    s = input()
    result_dict[s] += 1
 
print('AC'+' x '+str(result_dict['AC']))
print('WA'+' x '+str(result_dict['WA']))
print('TLE'+' x '+str(result_dict['TLE']))
print('RE'+' x '+str(result_dict['RE']))
