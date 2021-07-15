import sys
from collections import deque

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
    
mid_warms_deque = deque(sorted(mid_warms, reverse=True))
cold_days_nr = sum(colds)
free_days = k - cold_days_nr

if free_days < 0:
    print(-1)
    return
elif free_days == 0:
    print(switches_made)
    return
elif len(mid_warms) > 0:
    while mid_warms_deque:
        curr_warm_len = mid_warms_deque.pop()
        if not free_days - curr_warm_len >= 0:
            break
        switches_made -= 2
        free_days -= curr_warm_len
        
if free_days - last_warm >= 0:
    switches_made -= 1
    free_days -= last_warm
    
print(switches_made)
    

    

