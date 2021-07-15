current = input()
sleep = input()

hour_current = current[:current.index(':')]
min_current = current[current.index(':')+1:]

hour_sleep = sleep[:sleep.index(':')]
min_sleep = sleep[sleep.index(':')+1:]

current_in_min = int(hour_current)*60 + int(min_current)
sleep_in_min = int(hour_sleep)*60 + int(min_sleep)

bed_time = current_in_min - sleep_in_min
if bed_time < 0 :
    bed_time = 24*60 + bed_time
    out_hour = bed_time // 60
    out_min = bed_time % 60
else:
    out_hour = bed_time // 60
    out_min = bed_time % 60
if out_hour < 10 :
    out_hour = "0"+str(out_hour)
if out_min < 10 :
    out_min = "0" + str(out_min)
print(str(out_hour) + ":" + str(out_min))

