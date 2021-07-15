d={'SUN':1,'MON':2,'TUE':3,'WED':4,'THU':5,'FRI':6,'SAT':7}
today_key = input()
today_value = d[today_key]
nextsunday_value = 8-today_value
print(nextsunday_value)
