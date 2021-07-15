def resolve():
    weather = ['Sunny','Cloudy','Rainy']
    s = input()
    print(weather[(weather.index(s)+1)%3])
resolve()
