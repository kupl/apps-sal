n = int(input())

travel_times = list()
travel_pay = list()

pay_ticket1 = 0
time_ticket1 = 0

pay_ticket2 = 0
time_ticket2 = 0

for travel_id in range(n):
    t = int(input())
    travel_times.append(t)

    pay2 = 20

    sum_time1 = t - travel_times[time_ticket1]
    sum_time2 = t - travel_times[time_ticket2]

    if sum_time1 >= 90:
        pay_ticket1 -= travel_pay[time_ticket1]

        for id2 in range(time_ticket1 + 1, travel_id + 1):
            if t - travel_times[id2] < 90:
                time_ticket1 = id2
                break
            else:
                pay_ticket1 -= travel_pay[id2]

        sum_time1 = t - travel_times[time_ticket1]

    if sum_time2 >= 1440:
        pay_ticket2 -= travel_pay[time_ticket2]

        for id2 in range(time_ticket2 + 1, travel_id + 1):
            if t - travel_times[id2] < 1440:
                time_ticket2 = id2
                break
            else:
                pay_ticket2 -= travel_pay[id2]

        sum_time2 = t - travel_times[time_ticket2]

    if pay_ticket1 + pay2 > 50:
        pay2 = 50 - pay_ticket1

    if pay_ticket2 + pay2 > 120:
        pay2 = 120 - pay_ticket2

    pay_ticket1 += pay2
    pay_ticket2 += pay2

    travel_pay.append(pay2)

for pay in travel_pay:
    print(pay)
