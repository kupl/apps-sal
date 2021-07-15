from itertools import accumulate
n, m  = list(map(int, input().split()))

tt = n//2 +1
moments = [0] + list(map(int, input().split())) + [m]
times = [moments[i] - moments[i-1] for i in range(1,n+2)]
# print(times)
light = times[::2]
dark = times[1::2]

light_time = list(accumulate(light))
dark_time  = [0]+ list(accumulate(dark))
# print(light_time, dark_time)
res = light_time[-1]
for i in range(tt):
    if times[2*i] >1: # если горит больше минуты
        # print('light to ', i, ' is ', light_time[i]-1, dark_time[-1]-dark_time[i], 'if switching light off')

        res = max(res, light_time[i]-1 + (dark_time[-1]-dark_time[i]))

    if i == 0 or times[2*i-1] >1: # если не горит больше минуты
        # print('light to ', i, ' is ', light_time[i], dark_time[-1]-dark_time[i] -1)

        res = max(res, light_time[i] + dark_time[-1]-dark_time[i] -1)
print(res)
