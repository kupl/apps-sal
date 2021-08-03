no_of_alarms = int(input())

x_set = set()
y_set = set()
while no_of_alarms > 0:
    i_alarm = input().split()

    x_set.add(int(i_alarm[0]))
    y_set.add(int(i_alarm[1]))

    no_of_alarms = no_of_alarms - 1

if len(x_set) <= len(y_set):
    print(len(x_set))
else:
    print(len(y_set))
