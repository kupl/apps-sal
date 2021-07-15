def solve():

    a, b, f, k = [int(st) for st in input().split(" ")]

    fuel = b
    location = 0
    direction = "right"
    fueled = 0

    journeypassed = 0
    while journeypassed < k:

        #print("location:", location, ", fuel:", fuel, ", "+direction)

        if location == 0:
            if fuel < f:
                return -1
            fuel -= f
            location = f
            direction = "right"

        elif location == a:
            if fuel < a-f:
                return -1
            fuel -= a-f
            location = f
            direction = "left"

        elif location == f:
            
            if k - journeypassed <= 1:
                if direction == "left":
                    if fuel < f:
                        fuel = b
                        fueled += 1
                    if fuel < f:
                        return -1
                    fuel -= f
                    location = 0
                    direction = "right"
                else:
                    if fuel < a-f:
                        fuel = b
                        fueled += 1
                    if fuel < a-f:
                        return -1
                    fuel -= a-f
                    location = a
                    direction = "left"
                    
            else:
                if direction == "left":
                    if fuel < 2*f:
                        fuel = b
                        fueled += 1
                    if fuel < 2*f:
                        return -1
                    fuel -= 2*f
                    direction = "right"
                else:
                    if fuel < 2*(a-f):
                        fuel = b
                        fueled += 1
                    if fuel < 2*(a-f):
                        return -1
                    fuel -= 2*(a-f)
                    direction = "left"
                    
            journeypassed += 1
                    

    return fueled

print(solve())

