hoursmin = input()
hours = int(hoursmin[:2])
minutes = int(hoursmin[3:])
a = int(input())
new_hours = str((hours * 60 + minutes + a) // 60 % 24)
new_minutes = str((hours * 60 + minutes + a) % 60)
if len(new_hours) == 1:
    new_hours = '0' + new_hours
if len(new_minutes) == 1:
    new_minutes = '0' + new_minutes
print('{}:{}'.format(new_hours, new_minutes))
