data = input()
data = data.split()
rides_num = int(data[0])
ticket_rides = int(data[1])
ticket_price = int(data[3])
one_ride = int(data[2])
ticket_one_price = ticket_price / ticket_rides
sum = 0
if ticket_one_price < one_ride:
    num_of_tickets = int(rides_num / ticket_rides)
    sum += num_of_tickets * ticket_price
    rest = rides_num - num_of_tickets * ticket_rides
    if rest * one_ride < ticket_price:
        sum += rest * one_ride
    else:
        sum += ticket_price
    print(sum)
else:
    print(rides_num * one_ride)
