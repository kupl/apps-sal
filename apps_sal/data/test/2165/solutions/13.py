def get_max_volume(sources, required_temperature):
    """
    :param List[Set[int]]sources:
    :param int required_temperature:
    :return: float
    """
    max_volume = 0.
    temp = 0
    higher_sources = []
    lower_sources = []

    for volume, temperature in sources:
        delta_temp = temperature - required_temperature
        if delta_temp > 0:
            higher_sources.append((volume, delta_temp))
        elif delta_temp < 0:
            lower_sources.append((volume, delta_temp))
        max_volume += volume
        temp += volume * delta_temp
    higher_sources.sort(key=lambda v: v[1])
    lower_sources.sort(key=lambda v: -v[1])
    while abs(temp / max_volume) >= 1e-6 \
            and (len(lower_sources) > 0 or temp >= 0)\
            and (len(higher_sources) > 0 or temp <= 0):
        if temp < 0:
            volume, delta_temp = lower_sources.pop()
            if temp - delta_temp * volume >= 0:
                required_volume = temp / delta_temp
                return max_volume - required_volume
            temp -= delta_temp * volume
            max_volume -= volume
        else:
            volume, delta_temp = higher_sources.pop()
            if temp - delta_temp * volume <= 0:
                required_volume = temp / delta_temp
                return max_volume - required_volume
            temp -= delta_temp * volume
            max_volume -= volume

    if abs(temp / max_volume) < 1e-6:
        return max_volume

    return 0.


n, t = list(map(int, input().split()))
vs = input().split()
ts = input().split()
ss = [(int(vs[i]), int(ts[i])) for i in range(n)]
print(get_max_volume(ss, t))

