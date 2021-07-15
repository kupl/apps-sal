import sys

def weather(temp):
    return temp >= 0
    
INF = int(1e+6)
n, k = (int(x) for x in input().split())
day_to_temp = [int(x) for x in input().split()]
day_to_weather = [weather(temp) for temp in day_to_temp]

first_warm = -1
mid_warms = []
colds = []
curr_state = 0
curr_len = 0
switches_made = 0

for weather in day_to_weather:
    if curr_state == 0:
        if weather == 1:
            curr_len += 1
        else:
            first_warm = curr_len
            curr_state = 2
            curr_len = 1
            switches_made += 1
    elif curr_state == 1:
        if weather == 1:
            curr_len += 1
        else:
            mid_warms.append(curr_len)
            curr_state = 2
            curr_len = 1
            switches_made += 1
    else:
        if weather == 1:
            colds.append(curr_len)
            curr_state = 1
            curr_len = 1
            switches_made += 1
        else:
            curr_len += 1


if curr_state == 1:
    last_warm = curr_len
elif curr_state == 2:
    colds.append(curr_len)
    last_warm = INF
else:
    print(0)
    return
    
mid_warms = sorted(mid_warms)
cold_days = sum(colds)
free_days = k - cold_days

if free_days < 0:
    print(-1)
    return
elif free_days == 0:
    print(switches_made)
    return
elif len(mid_warms) > 0:
    i = 0
    while i < len(mid_warms) and free_days - mid_warms[i] >= 0:
        switches_made -= 2
        free_days -= mid_warms[i]
        i += 1
        
if free_days - last_warm >= 0:
    switches_made -= 1
    free_days -= last_warm
    
print(switches_made)
    

    

