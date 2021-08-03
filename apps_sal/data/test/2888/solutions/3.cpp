#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fastIO ios_base::sync_with_stdio(false); cin.tie(NULL)

ll n, s;
ll e[5004];
ll tval[5004];
int mp[5004][5004];

ll increased(ll s) {
    int s2 = s;
    int digSum = 0;
    while (s > 0) {
        digSum += s % 10;
        s /= 10;
    }
    return s2 + (ll)pow(digSum, 3);
}

ll f(int t, int i) {  // curr strength, no of times pikachu has been trained
    if (i == n) {
        return 0;
    }
    if (mp[t][i]) {
        return mp[t][i];
    }
    return mp[t][i] = max( f(t+1, i+1) , f(t, i+1) + tval[t]*e[i]);
}

int main() {
    
    fastIO;
    
    cin >> n >> s;
    for (int i=0; i<n; i++) {
        cin >> e[i];
    }
    
    tval[0] = s;
    for (int i=1; i <= n; i++) {
        tval[i] = increased(tval[i-1]); 
    }
    
    ll ans = f(0, 0);
    cout << ans;
    
	return 0;
}

